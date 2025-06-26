import speech_recognition as sr
import logging
logger = logging.getLogger(__name__)

def listen():
    logger.debug("Initializing microphone...")
    try:
        with sr.Microphone() as source:
            logger.debug("Listening for voice input...")
            audio = r.listen(source)
            logger.debug("Audio captured")
            return audio
    except Exception as e:
        logger.error(f"Microphone error: {str(e)}")
        raise