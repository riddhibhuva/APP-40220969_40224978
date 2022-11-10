import java.net.HttpURLConnection;
        import java.net.URL;
        import java.util.Scanner;
        import org.json.simple.JSONArray;
        import org.json.simple.JSONObject;
        import org.json.simple.parser.JSONParser;

public class Test {

    public static void main(String[] args) {
        try {

            URL url = new URL("https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key=BAtqzn48JznaNm0exY8xVdkqJQqWpLFA");

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.connect();

            //Getting the response code
            int responsecode = conn.getResponseCode();
            System.out.println(responsecode);
            if (responsecode != 200) {
                throw new RuntimeException("HttpResponseCode: " + responsecode);
            } else {

                String inline = "";
                Scanner scanner = new Scanner(url.openStream());

                //Write all the JSON data into a string using a scanner
                while (scanner.hasNext()) {
                    inline += scanner.nextLine();
                }

                //Close the scanner
                scanner.close();


                //Using the JSON simple library parse the string into a json object
                JSONParser parse = new JSONParser();
                JSONObject data_obj = (JSONObject) parse.parse(inline);
//
//                //Get the required object from the above created object
//                JSONObject obj = (JSONObject) data_obj.get("Headline");
//
//                //Get the required data using its key
//                System.out.println(obj.get("main"));

                JSONArray arr = (JSONArray) data_obj.get("headline");

                for (int i = 0; i < arr.size(); i++) {

                    JSONObject new_obj = (JSONObject) arr.get(i);

                    if (new_obj.get("Kicker").equals("Five places")) {
                        System.out.println("Headline is: " + new_obj.get("print_headline"));
                        break;
                    }
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
