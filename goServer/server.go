package main

import (
	"net/http"
)

func serverStart(w http.ResponseWriter, r *http.Request) {
	toSend := r.URL.Path
	toSend = "Hello from path " + toSend
	w.Write([]byte(toSend))
}

func main() {
	http.HandleFunc("/", serverStart)
	if err := http.ListenAndServe(":8080", nil); err != nil {
		panic(err)
	}
}
