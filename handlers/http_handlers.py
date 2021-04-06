from http import HTTPStatus

def success_request(content):
    return {
        'data': content
    }

def created_request():
    return 'Lead cadastrado com sucesso', HTTPStatus.CREATED

def unprocessable_request():
    return 'Este lead já está cadastrado', HTTPStatus.UNPROCESSABLE_ENTITY