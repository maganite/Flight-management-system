import json
import requests

from loguru import logger

from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.flight.models import FlightSensorData
from apps.utils.utils import CSRFExemptMixin, SideBarSelectedMixin
from .models import Flight
from .forms import FlightForm


class ActiveFlightListView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.ListView
):
    template_name = "pages/flights/active.html"
    model = Flight
    context_object_name = "flight_list"
    success_url = "bot:bot_list"
    parent = "flight"
    segment = "active_flight_list"
    paginate_by = 6


class InActiveFlightListView(
    LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView
):
    template_name = "pages/flights/inactive.html"
    # model = Bot
    # context_object_name = "bot_list"
    success_url = "bot:bot_list"
    parent = "flight"
    segment = "inactive_flight_list"
    # paginate_by = 6


class CreateFlightView(LoginRequiredMixin, SideBarSelectedMixin, generic.CreateView):
    template_name = "pages/flights/create_flight.html"
    parent = "flight"
    segment = "active_flight_list"
    form_class = FlightForm
    model = Flight
    success_url = reverse_lazy("flight:active_flight_list")

    def form_valid(self, form):
        # Save the new flight to the database
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     context = super(CreateTelegramBot, self).get_context_data(**kwargs)
    #     context["parent"] = self.parent
    #     context["segment"] = self.segment
    #     return context

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         bot = form.save(user=request.user)
    #         return super().form_valid(form)
    #     else:
    #         return super().form_invalid(form)


class UpdateFlightView(LoginRequiredMixin, SideBarSelectedMixin, generic.TemplateView):
    template_name = "pages/flights/edit_fligth.html"
    # model = Bot
    # form_class = BotForm
    parent = "bot"
    segment = "bot_list"
    # pk_url_kwarg = "id"
    success_url = reverse_lazy("bot:bot_list")

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateTelegramBotView, self).get_context_data(**kwargs)
    #     context["parent"] = self.parent
    #     context["segment"] = self.segment
    #     return context

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.form_class(request.POST, instance=self.object)
    #     if form.is_valid():
    #         bot = form.save(user=request.user)
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.form_invalid(form)


class GetDataFromSensor(CSRFExemptMixin, SideBarSelectedMixin, View):
    def post(self, request, **kwargs):
        try:
            id = kwargs.get("id")
            flight_sensor_data, _ = FlightSensorData.objects.get_or_create(flight_schedule_id=id)
            data = json.loads(request.body.decode("utf-8"))
            flight_sensor_data.current_gps = {
                "lat": data.get("lat"),
                "lon": data.get("lon"),
            }
            flight_sensor_data.current_temperature = data.get("engine_temp")
            flight_sensor_data.current_humidity = 0
            flight_sensor_data.current_speed = data.get("airspeed")
            flight_sensor_data.current_altitude = data.get("alt")
            flight_sensor_data.metadata = data
            flight_sensor_data.save()
            return JsonResponse(data)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"error": "Internal Server Error"}, status=500)

    def get(self, request):
        return JsonResponse(
            {"message": "GET method not supported for data submission"}, status=405
        )
