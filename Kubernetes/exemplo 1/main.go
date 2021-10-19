import "net/http"

func main() {

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader([]byte("OK"))
	})
	http.ListenAndServe(":8080", nil)
}