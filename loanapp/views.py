from django.shortcuts import render
from .models import LoanApplication

def loan_prediction(request):
    if request.method == "POST":
        income = float(request.POST['income'])
        credit_score = int(request.POST['credit_score'])
        loan_amount = float(request.POST['loan_amount'])
        employment_status = request.POST['employment_status']

        if credit_score >= 700 and income >= loan_amount:
            result = "Approved"
        else:
            result = "Rejected"

        loan = LoanApplication.objects.create(
            applicant_income=income,
            credit_score=credit_score,
            loan_amount=loan_amount,
            employment_status=employment_status,
            prediction_result=result
        )

        return render(request, "result.html", {"loan": loan})

    return render(request, "index.html")



