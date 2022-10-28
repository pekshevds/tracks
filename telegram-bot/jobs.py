def send_hello(context):
    print(dir(context.job))
    print('*' * 20)

    context.bot.send_message(
        chat_id=628400940,
        text=f"Привет {context.job.interval}!"
    )
    """context.job.interval += 5
    if context.job.interval > 15:

        context.bot.send_message(
            chat_id=628400940,
            text="Задание выполнено"
        )
        context.job.schedule_removal()"""
