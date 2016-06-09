FROM busybox

RUN mkdir -p /var/lib/appdata
WORKDIR /var/lib/appdata

COPY . /var/lib/appdata
VOLUME ['/var/lib/appdata']

CMD echo App Data container
