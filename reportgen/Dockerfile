FROM public.ecr.aws/lambda/python:latest
COPY . ${LAMBDA_TASK_ROOT}
RUN pip3 install -r requirements.txt
RUN yum install -y https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.amazonlinux2.x86_64.rpm
RUN yum install -y which
CMD ["lambda_function.lambda_handler"]