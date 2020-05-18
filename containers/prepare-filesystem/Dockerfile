FROM alpine:3
COPY ./prepare-filesystem.sh /prepare-filesystem.sh
RUN chmod +x /prepare-filesystem.sh
RUN apk add --no-cache --upgrade bash
CMD ["/prepare-filesystem.sh"]