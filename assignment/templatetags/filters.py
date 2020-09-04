from django import template
from assignment.models import Assignment, SelectCourse, StudentOtherCourse
from django.contrib.auth import get_user_model
import urllib
register = template.Library()

User = get_user_model()

@register.simple_tag
def count_assignment_of_student(pk):
    u = User.objects.get(pk=pk)
    a = Assignment.objects.filter(index=u).count()
    return a

@register.filter
def encode_id(pk):
    p = urllib.parse.urlencode(pk)
    return p
    

@register.simple_tag
def cal_course(pk):
    s = SelectCourse.objects.get(pk=pk)
    # o_c = StudentOtherCourse.objects.get(pk=pk)
    # u = User.objects.exclude(pk=s.pk).filter(course=s.courses).count()
    all_staff = User.objects.filter(is_staff=True)
    print(all_staff)
    o = StudentOtherCourse.objects.exclude(user__in=all_staff).filter(choose_course=s.courses).count()
    return o


@register.simple_tag
def courses():
    o_c = StudentOtherCourse.objects.all()
    return o_c
