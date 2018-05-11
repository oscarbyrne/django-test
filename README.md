# Background
In this example we have been brought in to test the hot new BAAS startup "buttly".
We brought with us the core application (contained in the module 'core'), and have extended it with the butt application. These are aggregated in the 'ion' project.


## Scenarios
Django can provide a GUI if required, or the tests can be run headless via calls to the service layer.
Models can be fetched from the database (grid mode), or else created on an ad-hoc basis with no database record (local bench / mocks).


## Demo
```
pip install -r requirements.txt
python sample.py
```


## Literature
For model / domain layer stuff:
- http://blog.joncairns.com/2013/04/fat-model-skinny-controller-is-a-load-of-rubbish/
- https://martinfowler.com/bliki/AnemicDomainModel.html
- https://stackoverflow.com/questions/22132563/domain-model-and-service-layer-patterns-in-p-of-eaa