from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='maxi-card.py',
  version='1.0.5',
  description='This is simple maker for cards welcome and leave in discord bot.',
  long_description=open('README.rst').read(),
  url='',  
  author='Maxi_TM',
  author_email='maksymilianratajczak794@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='discord welcome card',
  package_data={
    "maxicard": ["fonts/*.ttf", "imgs/*.png"],
  },
  packages=find_packages(),
  install_requires=['Pillow','easy-pil==0.1.6'] 
)
