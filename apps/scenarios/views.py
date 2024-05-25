from django.http import JsonResponse, request
from django.views import View
from apps.scenarios.models import Recommendation


class GetImpactView(View):
    def get(self, request, risk_type):
        recommendations = Recommendation.objects.filter(risk_type=risk_type)
        if recommendations.exists():
            recommendation = recommendations.first()
            return JsonResponse(recommendation.impact)
        else:
            return JsonResponse({'error': f'No recommendations found for risk type {risk_type}'})


class GetRecommendationView(View):
    def get(self, request, risk_type):
        recommendations = Recommendation.objects.filter(risk_type=risk_type)
        if recommendations.exists():
            recommendation = recommendations.first()
            return JsonResponse(recommendation.recommendation)
        else:
            return JsonResponse({'error': f'No recommendations found for risk type {risk_type}'})


class GetImpactAndRecommendationView(View):
    def get(self, request, risk_type):
        recommendations = Recommendation.objects.filter(risk_type=risk_type)
        if recommendations.exists():
            recommendation = recommendations.first()
            data = {
                'impact': recommendation.impact,
                'recommendation': recommendation.recommendation
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': f'No recommendations found for risk type {risk_type}'})
