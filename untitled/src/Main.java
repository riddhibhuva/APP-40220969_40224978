import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException{
//        System.out.println("Hello world!");
        var request = HttpRequest.newBuilder().GET().uri(URI.create("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=BAtqzn48JznaNm0exY8xVdkqJQqWpLFA")).build();
        var client = HttpRequest.newBuilder().build();
        var response = client.send(request, HttpRequest.BodyHandlers.ofString());
        System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}