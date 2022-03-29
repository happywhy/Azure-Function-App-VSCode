package FunctionAPP;

import java.util.*;
import com.microsoft.azure.functions.annotation.*;
import com.microsoft.azure.functions.*;
import com.microsoft.azure.functions.HttpResponseMessage;

public class ArraySum {
 /**
 * This function listens at endpoint "/api/DoubleValue". Two ways to invoke it using "curl" command in bash:
 * 1. curl -d "HTTP Body" {your host}/api/DoubleValue
 * 2. curl {your host}/api/DoubleValue?name=HTTP%20Query
 */
@FunctionName("ArraySum")
public HttpResponseMessage arraysum(
        @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.ANONYMOUS) HttpRequestMessage<List<Integer>> request,
        final ExecutionContext context) {
    context.getLogger().info("This is my java DoubleValue APP.");

    final List<Integer> val = request.getBody();
    int sumall =0;
    for (int i=0;i<val.size();i++) 
    {
        sumall = val.get(i)+sumall;
    }

    return request.createResponseBuilder(HttpStatus.OK).body("Double Value is: " + sumall).build();
}   
}
