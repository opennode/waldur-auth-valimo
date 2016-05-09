from __future__ import unicode_literals

from nodeconductor.core import NodeConductorExtension


class AuthValimoExtension(NodeConductorExtension):

    class Settings:
        NODECONCUTOR_AUTH_VALIMO = {
            'URL': None,
            'AP_ID': None,
            'AP_PWD': None,
            'DNSName': '',
            'SignatureProfile': None,
            'cert_path': None,
            'key_path': None,
            'message_prefix': 'Login code:',
        }

    @staticmethod
    def django_app():
        return 'nodeconductor_auth_valimo'

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in

    @staticmethod
    def celery_tasks():
        from datetime import timedelta
        return {
            'valimo-auth-cleanup-auth-results': {
                'task': 'nodeconductor.valimo_auth.cleanup_auth_results',
                'schedule': timedelta(hours=1),
            },
        }
