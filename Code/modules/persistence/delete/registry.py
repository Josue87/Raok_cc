from modules._module import AgentModule
from utils.custom_print import print_info, print_error, print_ok
from utildata.dataset_options import Option
from utils.redteam_db import RedTeamDB
from utils.check_agent import is_agent_alive


class RedTeamModule(AgentModule):

    def __init__(self):
        information = {"Name": "DeletePersistenceReg",
                       "Description": "With this module you will be able to Delete the persistence.",
                       "Author": "@josueencinar"}

        options = { }

        # Constructor of the parent class
        super(RedTeamModule, self).__init__(information, options)

    @is_agent_alive
    def run(self):
        rt_db = RedTeamDB.get_instance()
        rt_db.add_task(self.args["agent"], "DeletePersistenceReg", "", "", "function")
        print_info("Running Module")
      