!mkdir datasets
%cd datasets

!mkdir Images
!mkdir Labels

%cd Images

!wget https://zenodo.org/record/3762320/files/training.zip
!unzip training.zip

!wget https://zenodo.org/record/3762320/files/test.zip
!unzip test.zip

!rm training.zip
!rm test.zip

!mkdir ../Labels/training
!mkdir ../Labels/test

%cd ../