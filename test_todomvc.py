from time import time
from selene import browser, have, be, command

def test_complete_todo():

    browser.driver.execute_script(
        'document.qerySelector("#footer").remove'
    )
    browser.element('#footer').execute_script('element.remove()')
    browser.element('#footer').perform(command)

    browser.open('/')
    '''
    browser.should(have.title('Ember TodoMVC'))
    browser.element('#new-todo').should(be.blank)
    
    '''
    browser.element('#new-todo').type('first').press_enter()
    browser.element('#new-todo').type('second').press_enter()
    browser.element('#new-todo').type('third').press_enter()
    browser.all('#todo-list li').should(have.exact_texts('first', 'second', 'third'))
    '''
    browser.all('#todo-list li').should(have.texts('first', 'second', 'third'))
    browser.all('#todo-list li').should(have.size(3))
    browser.all('#todo-list li').first.should(have.exact_text('first'))
    browser.all('#todo-list li')[1].should(have.exact_text('second'))
    browser.all('#todo-list li')[2].should(have.exact_text('third'))
    unique_todo = f'test todo {time()}'
    browser.element('#new-todo').type(unique_todo).press_enter()
    browser.all('#todo-list li')[-1].should(have.exact_text(unique_todo))
    browser.all('#todo-list li').element_by(have.exact_text(unique_todo)).should(be.visible)
    browser.all('#todo-list li').by(have.exact_text(unique_todo)).should(have.size(1))
    '''
    browser.all('#todo-list li').element_by(have.exact_text('second')).element('.toggle').click()
    browser.all('#todo-list li').by(have.css_class('completed')).should(have.exact_texts('second')) # filter by all collections
    browser.all('#todo-list li').by(have.no.css_class('completed')).should(have.exact_texts('first' , 'third'))

    ...
