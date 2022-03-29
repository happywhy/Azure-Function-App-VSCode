package FunctionAPP;

import java.util.*;
import com.microsoft.azure.functions.annotation.*;
import com.microsoft.azure.functions.*;
import com.microsoft.azure.functions.HttpResponseMessage;

/**
 * Azure Functions with HTTP Trigger.
 */
public class DoubleValue {
    /**
     * This function listens at endpoint "/api/DoubleValue". Two ways to invoke it using "curl" command in bash:
     * 1. curl -d "HTTP Body" {your host}/api/DoubleValue
     * 2. curl {your host}/api/DoubleValue?name=HTTP%20Query
     */
    @FunctionName("DoubleValue")
    public HttpResponseMessage doublevalue(
            @HttpTrigger(name = "req", methods = {HttpMethod.GET, HttpMethod.POST}, authLevel = AuthorizationLevel.ANONYMOUS) HttpRequestMessage<Optional<String>> request,
            final ExecutionContext context) {
        context.getLogger().info("This is my java DoubleValue APP.");
        // int val = Integer.parseInt(request);
        // return 2*val;

        final String query = request.getQueryParameters().get("name");
        final String name = request.getBody().orElse(query);
        int val = Integer.parseInt(name)*2;

        return request.createResponseBuilder(HttpStatus.OK).body("Double Value is: " + val).build();
    }
}

