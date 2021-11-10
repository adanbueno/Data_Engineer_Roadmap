from flask import Flask,jsonify,request
import memory_profiler as mp
from memory_profiler import memory_usage
from memory_profiler import profile
from functools import wraps 
 
import memory_profiler
try:
    import tracemalloc
    has_tracemalloc = True
except ImportError:
    has_tracemalloc = False


def my_profiler(func=None, stream=None, precision=1, backend='psutil'):
    """
    Decorator that will run the function and print a line-by-line profile
    """
    backend = memory_profiler.choose_backend(backend)
    if backend == 'tracemalloc' and has_tracemalloc:
        if not tracemalloc.is_tracing():
            tracemalloc.start()
    if func is not None:
        @wraps(func)
        def wrapper(*args, **kwargs):
            prof = memory_profiler.LineProfiler(backend=backend)
            val = prof(func)(*args, **kwargs)
            memory_profiler.show_results(prof, stream=stream,
                                         precision=precision)
            return val

        return wrapper
    else:
        def inner_wrapper(f):
            return profile(f, stream=stream, precision=precision,
                           backend=backend)

        return inner_wrapper
 
 
app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Rafael Marques',
        'lang': 'python'
    },
    {
        'id': 2,
        'name': 'Robert Hrosher',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'John Delare',
        'lang': 'python'
    },
    {
        'id': 4,
        'name': 'John Doe',
        'lang': 'node'
    }
]

#@mp.profile
@app.route('/devs', methods=['GET'])
@my_profiler
def home():
    return jsonify(devs), 200


#@mp.profile
@app.route('/devs/<string:lang>', methods=['GET'])
@my_profiler
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


#@mp.profile
@app.route('/devs/<int:id>', methods=['PUT'])
@my_profiler
def change_lang(id):
    for dev in devs:
        if dev['id'] == id:
            dev['lang'] = request.get_json().get('lang')
            return jsonify(dev),200
        
    return jsonify({'message':'Dev not found'}),404


#@mp.profile
@app.route('/devs/<int:id>', methods=['GET'])
@my_profiler
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
        
    return jsonify({'error': 'Dev not found'}), 404

#@mp.profile
@app.route('/devs', methods=['POST'])
@my_profiler
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(data), 201



if __name__ == '__main__':
    app.run(debug=True)
    