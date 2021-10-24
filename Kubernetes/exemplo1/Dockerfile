FROM golang:1.16

COPY . . 

RUN go build -0 server main.go
CMD ["./server"]