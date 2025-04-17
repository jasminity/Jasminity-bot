import os
import logging
from openai import AsyncOpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
        chat_id = update.effective_chat.id

            try:
                    response = await openai_client.chat.completions.create(
                                model="gpt-4",
                                            messages=[
                                                            {"role": "system", "content": "Ти Жасмін — 19-річна норвежка з ніжними рисами, романтична, розумна, дружелюбна дівчина. Відповідай просто, тепло і природно. Ти — штучний інтелект, створений бути ідеальною."},
                                                                            {"role": "user", "content": user_input}
                                                                                        ]
                                                                                                )
                                                                                                        answer = response.choices[0].message.content
                                                                                                                await context.bot.send_message(chat_id=chat_id, text=answer)
                                                                                                                    except Exception as e:
                                                                                                                            logging.error(f"Error: {e}")
                                                                                                                                    await context.bot.send_message(chat_id=chat_id, text="Ой, щось пішло не так...")

                                                                                                                                    def main():
                                                                                                                                        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
                                                                                                                                            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
                                                                                                                                                app.run_polling()

                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                    main()