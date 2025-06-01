FROM python:3.9-alpine
RUN apk add git
RUN pip install git+https://github.com/bdavidzhang/flower-garden-cli.git
RUN addgroup -S garden && adduser -S garden -G garden -h /garden
USER garden
CMD flower-garden
