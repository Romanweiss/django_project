from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import asyncio


class AsyncPage(View):
    async def process_1(self, request):
        data = []
        for i in range(1, 100):
            data.append(i)
            await asyncio.sleep(0.0001)
        return data
    async def process_2(self, request):
        data = []
        for i in range(1000, 1300):
            data.append(i)
            await asyncio.sleep(0.0001)
        return data

    async def get(self, request):
        result = await asyncio.gather(
            self.process_1(request),
            self.process_2(request)
        )
        return HttpResponse(result)
