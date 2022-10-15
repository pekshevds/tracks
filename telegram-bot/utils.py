import settings
from random import choice, randint
from emoji import emojize

from telegram import ReplyKeyboardMarkup, keyboardbutton


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc, service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)    
        smile = emojize(smile)
        return smile
    return user_data['emoji']


def play_randon_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
    return message

def has_object_on_image(file_name, object_name):
    channel = ClarifaiChannel.get_grpc_channel()
    app = service_pb2_grpc.V2Stub(channel=channel)
    metadata = (('authorization', f'Key {settings.CLARIFAI_API_KEY}'),)

    with open(file_name, "rb") as file:
        file_data = file.read()
        image = resources_pb2.Image(base64=file_data)

    request = service_pb2.PostModelOutputsRequest(
        model_id='aaa03c23b3724a16a56b629203edc62c',
        inputs=[
            resources_pb2.Input(data=resources_pb2.Data(image=image))
        ])

    response = app.PostModelOutputs(request, metadata=metadata)
    return check_response_for_object(response, object_name)


def check_response_for_object(response, object_name):
    if response.status.code == status_code_pb2.SUCCESS:
        for concept in response.outputs[0].data.concepts:
            if concept.name == object_name and concept.value >= 0.9:
                return True
    else:
        print(f"Ошибка распозновая картинки {response.outputs[0].status.details}")
    return False 


def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Заполнить анкету']
    ])


if __name__ == "__main__":
    print(has_object_on_image("images/dog1.jpeg", "dog"))