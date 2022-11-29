FROM golang:1.13.1-alpine
WORKDIR /go/src/app
COPY . .
RUN go build -o server server.go

FROM alpine
WORKDIR /app
COPY --from=0 /go/src/app/server .
EXPOSE 8080
CMD ["./server"]