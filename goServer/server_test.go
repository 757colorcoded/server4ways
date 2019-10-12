package main

import (
    "net/http"
    "net/http/httptest"
    "testing"

	//go get
    "github.com/gorilla/mux"
    "github.com/stretchr/testify/assert"
)

func Router() *mux.Router {
    router := mux.NewRouter()
    router.HandleFunc("/", serverStart).Methods("GET")
    return router
}

func TestEndpoint(t *testing.T) {
    request, _ := http.NewRequest("GET", "/", nil)
    response := httptest.NewRecorder()
    Router().ServeHTTP(response, request)
    assert.Equal(t, 200, response.Code, "OK response is expected")
}