import java.io.IOException;
import java.net.URI;
import java.net.http.HttpRequest;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;

class request{public void get(String uri) throws Exception {
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(uri))
            .build();

    HttpResponse<String> response =
            client.send(request, HttpResponse.BodyHandlers.ofString());

    System.out.println(response.body());
}}

public class Main {
    public static void main(String[] args) throws Exception {
//        System.out.println("Hello world!");
//        var request = HttpRequest.newBuilder().GET().uri(URI.create("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=BAtqzn48JznaNm0exY8xVdkqJQqWpLFA")).build();
//        var client = HttpRequest.newBuilder().build();
//        var response = client.send(request, HttpRequest.BodyHandlers.ofString());
//        System.out.println(response.statusCode());
//        System.out.println(response.body());

        request r1 =new request();
        r1.get("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=BAtqzn48JznaNm0exY8xVdkqJQqWpLFA");
    }


}


