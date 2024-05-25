from __future__ import absolute_import, unicode_literals

import logging
import requests
from celery import shared_task

from .models import (
    ConversationProcessing,
    ConversationRole,
    ConversationHistory,
    ConversationProcessingStatus,
    Message,
    Bot,
)
from .utils.mapper import (
    message_to_conversation_history,
    tele_user_message_to_message_model,
    tele_model_message_to_message_model,
)
from config.settings.local import TELEGRAM_API_URL


logger = logging.getLogger(__name__)


def send_generated_reply(method, data, bot_id):
    logger.info(f"sending message: {data}")
    bot = Bot.objects.get(id=bot_id)
    return requests.post(f"{TELEGRAM_API_URL}{bot.bot_token}/" + method, data)


@shared_task()
def generate_and_send_response(process_id, bot_id):
    pass
