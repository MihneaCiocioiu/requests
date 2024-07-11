# Report for Assignment 1 resit

## Project chosen: requests

Name: Mihnea Ciocioiu

URL: https://github.com/MihneaCiocioiu/requests

Number of lines of code and the tool used to count it: 8188, lizard.py

Programming language: Python

## Coverage measurement with existing tool

Tool used: Coverage.py

Command used: ```coverage run -m pytest```

![image](https://github.com/MihneaCiocioiu/requests/assets/45711313/e0b2bf06-7558-4691-b7a3-d796d92681ec)

## Coverage improvement

## Individual tests

### First function: ```remove_cookie_by_name()```

[Commit link](https://github.com/psf/requests/commit/8e327ef5cd0ab2334f079b03dd3702a26820704f)

#### Function in ```coverage html``` before

![image](https://github.com/MihneaCiocioiu/requests/assets/45711313/6c31bf7a-4aef-4910-9549-b48b64da5fe1)

### Function in ```coverage html``` after

![image](https://github.com/MihneaCiocioiu/requests/assets/45711313/d187149e-378e-4952-990f-c9daa1cc35cd)

Before, when running the full coverage function, we are now getting ```596 passed```, in contrast with the ```590 passed``` from before, which shows an improvement with the added coveerage for our function.

```_find()```

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 1>

![image](https://github.com/MihneaCiocioiu/requests/assets/45711313/0b841ef4-e17d-4e19-8182-6449cf5b2c74)

<Provide a screenshot of the new coverage results for such function>

<State the coverage improvement with a number and elaborate on why the coverage is improved>


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed at the beginning of the report)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications>

