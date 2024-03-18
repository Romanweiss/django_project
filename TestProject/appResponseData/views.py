from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import GenerateTab
import random

class ResponsePage(View):
    def get(self, request):
        d1 = GenerateTab.objects.all()
        for item in d1:
            # print(item.number, item.status, item.id)
            if item.status:
                item.number += random.randint(1, 3)
            else:
                item.number -= random.randint(10, 11)
            item.save()

        # print(GenerateTab.objects.order_by('-number'))
        # d_gt = GenerateTab.objects.filter(number__gt=100_000)
        # print('Больше 100к', d_gt)
        # d_lt = GenerateTab.objects.filter(number__lt=100_000)
        # print('Меньше 100к', d_lt)
        
        # for item in d1:
        #     if item.number > 100000:
        #         print(item.number)

        data = {
            
        }
        data['generate_nums'] = GenerateTab.objects.values('id', 'number')
        print(data)
        
        # print(GenerateTab.objects.values_list('id', 'number'))

        

        return JsonResponse(data, safe=False)



