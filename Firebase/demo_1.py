from firebase import firebase
firebase = firebase.FirebaseApplication('https://nickdata.firebaseio.com', None)
result = firebase.get('/usuarios', None)
print (result[1]['nombre'])
