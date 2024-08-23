from django import template
import math
from courses.models import Course, UserCourse
register = template.Library() 

@register.simple_tag 
def cal_sell_price(price, discount):
    if discount is None or discount == 0:
        return price
    else:
        return math.floor(price - (price * discount / 100))
    

@register.filter
def rupee(price):
    return f'₹{price}'

@register.simple_tag 
def is_enrolled(request, course):
    user = None
    if not request.user.is_authenticated:
        return False
    user=request.user
    try:
        user_course= UserCourse.objects.get(user=user,course=course)
        return True
    except:
        return False