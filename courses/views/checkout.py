from time import  time 
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from courses.models.course import Course
from courses.models.video import Video  
from courses.models.payment  import Payment
from courses.models.user_course import UserCourse
from codewithvijay.settings import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
client=razorpay.Client(auth=(KEY_ID, KEY_SECRET))


def checkout(request, slug):
    course  = Course.objects.get(slug=slug)
    user=None
    if request.user.is_authenticated == False:
        return redirect('login')
    user=request.user
    order=None
    payment=None
    error=None
    action=request.GET.get('action')
    try:
        user_course = UserCourse.objects.get(user=user,course=course)
        error="Course is already purchased"
    except:
        pass
    if action == 'create_payment':
        amount=int((course.price -(course.price * course.discount *0.01)) * 100)
        currency = "INR"
        notes={
            "email":user.email,
            "name":f"{user.first_name} {user.last_name}"
        }
        receipt=f"vijay-{int(time())}"
        order=client.order.create(
            {
            'receipt':receipt,
            'notes':notes,
            'amount':amount,
            'currency':currency
            })
        payment=Payment()
        payment.user=user
        payment.course=course
        payment.order_id=order.get('id')
        payment.save()        
    context = {
        'course': course,
        'order': order,
        'payment': payment,
        'user':user,
        'error':error
    }
    return render(request, 'courses/check_out.html', context=context)

@csrf_exempt
def verify_payment(request):
    if request.method=='POST':
        data=request.POST
        context = {}
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.status=True
            payment.payment_id=razorpay_payment_id
            
            userCourse=UserCourse(user=payment.user,course=payment.course)
            userCourse.save()
            payment.user_course=userCourse
            payment.save()

            return render(request, template_name='courses/my_courses.html', context=context)
        except:
            return HttpResponse('Invalid Payment details')