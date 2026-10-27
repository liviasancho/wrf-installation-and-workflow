
import subprocess
# https://www.scrapingbee.com/blog/python-wget/#:~:text=Wget%20is%20a%20convenient%20solution,automated%20to%20save%20you%20time.
def terminal(cmd, verbose=False, *args, **kwargs):
    """
    Função para rodar terminal dentro do python
    """
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass