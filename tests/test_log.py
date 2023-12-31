from praetorian_api_client.resources.log import LogResource


class TestLog:
    def test_successful_create(self, api_client):
        remote_id = 'e6691ecd-e4d2-47c9-b498-e744cfd6a6ad'
        log = [
            {
                "timestamp": 1701246699.781255,
                "data": "Last login: Wed Nov 29 09:31:31 2023 from 10.253.1.65\r\r\nFreeBSD 13.2-RELEASE-p1 GENERIC\r\nDo you want to do a binary upgrade of your running FreeBSD installation? Use freebsd-update(8).\r\n\r\nTo install updates and patches for the running branch use\r\n# freebsd-update fetch install\r\n\r\nTo upgrade to a newer release use\r\n# freebsd-update upgrade -r ${name_of_release}\r\n\r\n\t\t-- Lars Engels <lme@FreeBSD.org>\r\n<ESC>[praetorian@praetorian ~]$ ",
                "type": "output",
                "prompt": "Input: "
            },
            {
                "timestamp": 1701246709.42558,
                "data": "su -\r",
                "type": "input",
                "prompt": "[praetorian@praetorian ~]$ "
            },
            {
                "timestamp": 1701246711.3381262,
                "data": "\r\n<ESC>\rsu: Sorry\r\n<ESC>[praetorian@praetorian ~]$ ",
                "type": "output",
                "prompt": "Input: "
            },
            {
                "timestamp": 1701246716.1509252,
                "data": "cd /usr/ports/editors/j<RemovedBeforeThis>oe\r",
                "type": "input",
                "prompt": "[praetorian@praetorian ~]$ "
            },
            {
                "timestamp": 1701246729.090813,
                "data": "\r\n<ESC>\r<ESC>[praetorian@praetorian /usr/ports/editors/joe]$ ",
                "type": "output",
                "prompt": "Input: "
            }
        ]

        log = api_client.log.create(remote_id=remote_id, base_log=log)

        assert (
                isinstance(log, LogResource.Log)
                and hasattr(log, 'id')
                and hasattr(log, 'remote_id')
                and hasattr(log, 'user_id')
                and hasattr(log, 'device_id')
                and hasattr(log, 'base_log')
        )
