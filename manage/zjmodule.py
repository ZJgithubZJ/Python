#
# Copyright 2019
# zj <zhangjian@xhhd.com>
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import func_module
from func.minion import sub_process

class Zjmodule(func_module.FuncModule):

    # Update these if need be.
    version = "0.0.1"
    api_version = "0.0.1"
    description = "test zj module"

    def echo(self,linecount):
        """
        TODO: response system messages info
        """
	command = "/usr/bin/tail -n "+str(linecount)+" /var/log/messages"
	cmdref = sub_process.Popen(command, stdout=sub_process.PIPE, stderr=sub_process.PIPE, shell=True, close_fds=True)
	data = cmdref.communicate()
	return (cmdref.returncode, date[0], data[1])
