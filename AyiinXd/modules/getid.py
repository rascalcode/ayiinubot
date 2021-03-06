from telethon.utils import pack_bot_file_id

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, LOGS
from AyiinXd.utils import edit_delete, edit_or_reply, ayiin_cmd
from AyiinXd.utils.logger import logging

LOGS = logging.getLogger(__name__)


@ayiin_cmd(pattern="(get_id|id)(?:\\s|$)([\\s\\S]*)")
async def _(event):
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{e}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"**User :** {input_str}\n"
                           f"**ID** ยป `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"**Name :** {p.title}\n"
                               f"**ID** ยป `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(event, "**Berikan Username atau Reply ke pesan pengguna**")
    elif event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                "**๐ฌ Message ID:** `{}`\n**๐โโ๏ธ From User ID:** `{}`\n**๐ Bot API File ID:** `{}`".format(
                    str(r_msg.id),
                    str(r_msg.sender_id),
                    bot_api_file_id,
                ),
            )

        else:
            await edit_or_reply(
                event,
                "**๐ฅ Chat ID:** `{}`\n**๐ฌ Message ID:** `{}`\n**๐โโ๏ธ From User ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.id), str(r_msg.sender_id)
                ),
            )

    else:
        await edit_or_reply(event, f"**๐ฅ Chat ID: **`{event.chat_id}`")


CMD_HELP.update(
    {
        "id": f"**Plugin : **`id`\
        \n\n  ยป  **Perintah :** `{cmd}id` <username/reply>\
        \n  ยป  **Kegunaan : **Untuk Mengambil Chat ID obrolan saat ini\
        \n\n  ยป  **Perintah :** `{cmd}userid` <username/reply>\
        \n  ยป  **Kegunaan : **Untuk Mengambil ID & Username obrolan saat ini\
    "
    }
)
