from server import api, session
from model import User, Log

def email_exists(email):
	return bool(session.query(User).filter(User.email == email).first())

def get_user_by_email(user_email):
	return session.query(User) \
		.filter(User.email == user_email) \
		.first()

def user_hash(user_email):
	return get_user_by_email(user_email).password

def user_last_login(user_email):
	return session.query(Log) \
		.join(User) \
		.filter(User.email == user_email) \
		.order_by(Log.date.desc()) \
		.first()

def user_by_uuid(user_id):
	return session.query(User) \
		.filter(User.uuid == user_id) \
		.first()