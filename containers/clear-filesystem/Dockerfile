FROM alpine:3
COPY ./clear-filesystem.sh /clear-filesystem.sh
RUN chmod +x /clear-filesystem.sh
RUN apk add --no-cache --upgrade bash
CMD ["/clear-filesystem.sh"]