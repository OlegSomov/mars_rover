Minimalistic readme

# Mars operation
Support python 3+
## To try it out
You can either
1. Run `python3.7 main.py" and enter the commands. For example as per spec.
```
5 5
1 2 N
LMLMLMLMM
```
2. Run from a file `python3.7 main.py /path/to/instructions.txt" this will output the final locations as per spec.

3. Run a docker image to run the commands
- `docker build .`
- `docker -t mars_operation . && docker run -it mars_operation`

## To run tests

You can run test locally or add this project to TravisCI
simply run (recommended to create a new virtualenv from python3.7)

```pip install -r requiremnts.txt && python -m pytest --cov= src/ --capture=sys --cov-report html ```

will provide html report