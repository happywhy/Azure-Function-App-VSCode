import logging
from mimetypes import init

import azure.functions as func
from shared_code import array_sum

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('This is array sum application......')


    # obtain the list of input
    initial_array: list = list(req.params.get('value'))

    # delete the left and right square brackets in the list
    initial_array.pop(0)
    len_arr = len(initial_array)
    initial_array.pop(len_arr-1)

    # delte all , in the list
    del_val = ','
    initial_array = [value for value in initial_array if value!=del_val]

    ini_arr = list(map(int,initial_array))

    # sumarize all the element
    sum_value: int = array_sum.sumall(ini_arr)

    return func.HttpResponse(
      body=f"The element sum is {sum_value}",
      status_code=200
    )
