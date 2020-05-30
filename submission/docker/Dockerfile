FROM python:3

ADD solution_script.py /

ADD sample_input.json /

ADD sample_output.json /

RUN  pip install pandas==1.0.4

CMD [ "python", "./solution_script.py", "sample_input.json", "sample_output.json" ]
