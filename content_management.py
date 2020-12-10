##// CURRENT:
##// list of topics by {TOPIC:[["TITLE", "URL"]]}
##
##// FUTURE:
##////list of topics by {TOPIC:[["TITLE", "URL", "TAGS"],
##////                          ["TITLE", "URL", "TAGS"]]}

def Content():
##    //             Suggest Branches for next steps
##    //             If liked: Matplotlib, link to data analysis or Pandas maybe
##    //             If liked: GUI stuff: Kivy, PyGame, Tkinter
##    //             if liked: Text and word-based: NLTK


    # MAIN : [TITLE, URL, BODY_TEXT (LIST), HINTS(LIST)]
    TOPIC_DICT = {"Basics":[["Python Introduction","/introduction-to-python-programming/",[""]],
                            ["Print Function and Strings","/python-tutorial-print-function-strings/",["The Print function outputs text to the console (black area). Let's try it out!","print() is a function, which does something with parameters, and parameters go inside the parenthesis.","See if you can use the print function to output 'Hello!' to the console!"]],
                            ["Math with Python","/math-basics-python-3-beginner-tutorial/"],
                            ["Variables","/python-3-variables-tutorial/"],
                            ["While Loop","/python-3-loop-tutorial/"],
                            ["For Loop","/loop-python-3-basics-tutorial/"],
                            ["If Statement","/if-statement-python-3-basics-tutorial/"],
                            ["If Else","/else-python-3-tutorial/"],
                            ["If Elif Else","/elif-else-python-3-tutorial/"],
                            ["Functions","/functions-python-3-basics-tutorial/"],
                            ["Function Parameters","/function-parameters-python-3-basics/"],
                            ["Function Parameter Defaults","/function-parameter-defaults-python-3-basics/"],
                            ["Global and Local Variables","/global-local-variables/"],
                            ["Installing Modules","/installing-modules-python-3/"],
                            ["How to download and install Python Packages and Modules with Pip ","/using-pip-install-for-python-modules/"],
                            ["Common Errors","/common-errors-python-3-basics/"],
                            ["Python 2to3 for Converting Python 2 scripts to Python 3","/converting-python2-to-python3-2to3/"]],
                  





                  

                  
                            }


    return TOPIC_DICT



if __name__ == '__main__':
  x = Content()


  print(x["basics"])

  for each in x["Basics"]:
    print(each[1])