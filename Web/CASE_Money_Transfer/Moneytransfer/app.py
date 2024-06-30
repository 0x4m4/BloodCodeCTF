from flask import Flask, render_template, session, request, jsonify, make_response
import random
import string

sal = string.ascii_letters+'0123456789'
balances = {}
app = Flask(__name__)
app.secret_key = 'XKfToYZ2ouOMWLtZpqYKXmlLsrFjNzHt0pqpbSmUzhpojne69NgHmi7KQLVw768n'
feedbacks = []
@app.route('/')
def index():
    if request.args.get('backdoor') == 'GfghT875T738KLDVSDKJrgiherUERT8589T704VWH4TV3TU3febgjer':
        session['userid'] = '00000'
    if session.get('userid') == '00000':
        session['balance'] = int(1e18)
        balances[session['userid']] = int(1e18)
    if not session.get('userid'):
        uid = ''
        for i in range(64):
            uid += sal[random.randint(0, len(sal)-1)]
        session['userid'] = uid
    if session['userid'] in balances:
        session['balance'] = balances[session['userid']]
    else:
        session['balance'] = 0
        balances[session['userid']] = 0

    context = {}
    uid = session['userid']
    context['userid'] = uid
    context['balance'] = session['balance']
    try:
        context['csrf_token'] = request.cookies.get("_xsrf").split('|')[2]
        session['csrf_token'] = context['csrf_token']
    except:
        context['csrf_token'] = 'WFKJfgr56546REGRGdsvdrt4RDVSDG'
        session['csrf_token'] = context['csrf_token']

    if uid == '00000':
        resp = make_response(render_template('index.html', context=context))
        resp.set_cookie('_xsrf', 'WFKJfgr56546REGRGdsvdrt4RDVSDG')
        return resp

    return render_template('index.html', context=context)


@app.route('/flag')
def flag():
    session['balance'] = balances.get(session['userid'], 0)
    if session['balance'] < 1000:
        return "<h2>Sorry you don't have sufficent balance to view the flag</h2>"
    else:
        return "flag{g1ve_m3_my_mon3y_b4ck}"


@app.route('/transfer')
def transfer():
    global balances
    recepient = request.args.get('userid')
    amount = request.args.get('amount')
    csrf_token = request.args.get('csrf_token')
    responsed = {}
    if not session['csrf_token'] == csrf_token:
        responsed['stat'] = 'err'
        responsed['msg'] = 'csrf token invalid'
        print(responsed)
        return jsonify(responsed)
    try:
        amount = int(amount)
        assert(amount >= 0)
    except:
        responsed['stat'] = 'err'
        responsed['msg'] = 'Amount is not a positive integer'
        print(responsed)
        return jsonify(responsed)
    if not recepient in balances:
        responsed['stat'] = 'err'
        responsed['msg'] = 'Recepient does not exist'
        print(responsed)
        return jsonify(responsed)

    if amount > session['balance']:
        print(amount, session['balance'])
        print(balances)
        responsed['stat'] = 'err'
        responsed['msg'] = 'You have insufficient balance for this transaction'
        print(responsed)
        return jsonify(responsed)

    balances[session['userid']] -= amount
    session['balance'] -= amount
    print(session['balance'], balances)
    balances[recepient] += amount
    responsed['stat'] = 'success'
    responsed['msg'] = 'Transaction successful'
    print(responsed)
    return jsonify(responsed)


@app.route('/feedback')
def feedback():
    context = {}
    uid = session['userid']
    context['userid'] = uid
    context['balance'] = session['balance']
    try:
        context['csrf_token'] = request.cookies.get("_xsrf").split('|')[2]
    except:
        context['csrf_token'] = 'WFKJfgr56546REGRGdsvdrt4RDVSDG'

    return render_template('feedback.html', context=context)


@app.route('/feedbacksubmit', methods=['POST'])
def feedbacksubmit():
    feedback = request.json['feedback']
    feedbacks.append(feedback)
    print(feedback, '\n', feedbacks)
    d = {'msg': 'Feedback submitted.'}
    return jsonify(d)


@app.route('/feedbackview')
def feedbackview():
    if session['userid'] != '00000':
        return 'Only admin can view user submitted feedback'
    else:
        feeds = '<html><head><title>Feedback View</title></head><body>'
        for e in feedbacks:
            feeds += e+'<br/>'
        feeds += '</body></html>'
        return feeds


if __name__ == '__main__':
    balances['00000'] = int(1e18)
    app.run(host="0.0.0.0")
