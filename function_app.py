import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    tenure = req.params.get("tenure")
    techsupport = req.params.get("techsupport")
    monthly = req.params.get("monthly")

    if tenure and techsupport and monthly:
        prediction = make_prediction(
            tenure=float(tenure),
            MonthlyCharges=float(monthly),
            TechSupport_yes=float(techsupport),
        )
        return func.HttpResponse(f"This customer is {prediction} likely to churn!")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass tenure, monthly and techsupport in the query string for a personalized response.",
            status_code=200,
        )
