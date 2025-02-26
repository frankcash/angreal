Angreal
=======

.. image:: https://gitlab.com/angreal/angreal/badges/master/pipeline.svg
    :target: https://gitlab.com/angreal/angreal/commits/master

.. image:: https://gitlab.com/angreal/angreal/badges/master/coverage.svg
    :target: https://gitlab.com/angreal/angreal/commits/master

.. image:: https://badge.fury.io/py/angreal.svg
    :target: https://badge.fury.io/py/angreal

Angreal is a tool for templating projects and associated processes to hopefully lessen the cognitive load that goes with project management.

Installation :

.. code-block:: bash

    pip install angreal>2


Development : 

.. code-block:: bash  
    
    #install as python wheel
    maturin develop

    #pytests
    maturin develop
    pip install pytest
    python -m pytest

    #run tests
    cargo test -- --test-threads=1 
    
    #rustfmt
    find . -name "*.rs" | xargs rustfmt

    #clippy

    cargo clippy --fix 
    
