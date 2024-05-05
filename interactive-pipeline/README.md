Designing and implementing machine learning pipelines can be frustrating at times. It is sometimes challenging to debug components within a pipeline, for example. This is why the TFX functionality around interactive pipelines is beneficial.

The interactive pipeline runs in a Jupyter Notebook, and the components’ artifacts can be immediately reviewed. Once we have confirmed the full functionality of our pipeline,we can convert the interactive pipeline to a production-ready pipeline, for example, for execution on Apache Airflow.

Any interactive pipeline is programmed in the context of a Jupyter Notebook or a Google Colab session. In contrast to the orchestration tools interactive pipelines are orchestrated and executed by the user.