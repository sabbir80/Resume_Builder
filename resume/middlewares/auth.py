from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('middleware')
        print(request.session.get('user_id'))
        if not request.session.get('user_id'):
            return redirect('login')

        response = get_response(request)

        return response

    return middleware