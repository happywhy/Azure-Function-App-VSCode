import logging
from azure.functions import func

def test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('This is array sum application......')
 
    value=req.params.get('value')
    
    initial_array = list(value)
    sum_value: list = sumall(initial_array)

    return func.HttpResponse(
      body=f"The element sum of {initial_array} is {sum_value}",
      status_code=200
    )
def sumall(arr: list)->int:
    if len(arr)==0:
        return 0
    idx = 0
    total_sum = arr.pop(idx)
    if len(arr)==0:
        return total_sum
    else:
        return total_sum+sumall(arr)

req = func.HttpRequest(
            method='GET',
            url='.',
            body=None,
            params={'value': [1,2,3,4,5,6]}
            )
resp = test(req)

print(resp.get_body())