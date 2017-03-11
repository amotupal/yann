from yann.utils.dataset import setup_dataset

def cook_mnist_normalized(  verbose = 1, **kwargs):
    """
    Wrapper to cook mnist dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`

    Notes:
        By default, this will create a dataset that is not mean-subtracted.
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                   "source"             : 'skdata',
                   "name"               : 'mnist',
                   "location"			: '',
                   "mini_batch_size"    : 500,
                   "mini_batches_per_batch" : (100, 20, 20),
                   "batches2train"      : 1,
                   "batches2test"       : 1,
                   "batches2validate"   : 1,
                   "height"             : 28,
                   "width"              : 28,
                   "channels"           : 1  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

    # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : True,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : False,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                            save_directory = save_directory,
                            preprocess_init_args = preprocess_params,
                            verbose = 3)
    return dataset

def cook_mnist_normalized_zero_mean(  verbose = 1,	**kwargs):
    """
    Wrapper to cook mnist dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                   "source"             : 'skdata',
                   "name"               : 'mnist',
                   "location"			: '',
                   "mini_batch_size"    : 500,
                   "mini_batches_per_batch" : (100, 20, 20),
                   "batches2train"      : 1,
                   "batches2test"       : 1,
                   "batches2validate"   : 1,
                   "height"             : 28,
                   "width"              : 28,
                   "channels"           : 1  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

    # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : True,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : True,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                            save_directory = save_directory,
                            preprocess_init_args = preprocess_params,
                            verbose = 3)
    return dataset

def cook_mnist_multi_load(  verbose = 1, **kwargs):
    """
    Testing code, mainly.
    Wrapper to cook mnist dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`

    Notes:
        This just creates a ``data_params`` that loads multiple batches without cache. I use this
        to test the cahcing working on datastream module.
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                   "source"             : 'skdata',
                   "name"               : 'mnist',
                   "location"			: '',
                   "mini_batch_size"    : 500,
                   "mini_batches_per_batch" : (20, 5, 5),
                   "batches2train"      : 5,
                   "batches2test"       : 4,
                   "batches2validate"   : 4,
                   "height"             : 28,
                   "width"              : 28,
                   "channels"           : 1 }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():
        # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : True,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : False,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                            save_directory = save_directory,
                            preprocess_init_args = preprocess_params,
                            verbose = 3)
    return dataset

def cook_cifar10_normalized(verbose = 1, **kwargs):
    """
    Wrapper to cook cifar10 dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                   "source"             : 'skdata',
                   "name"               : 'cifar10',
                   "location"			: '',
                   "mini_batch_size"    : 500,
                   "mini_batches_per_batch" : (80, 20, 20),
                   "batches2train"      : 1,
                   "batches2test"       : 1,
                   "batches2validate"   : 1,
                   "height"             : 32,
                   "width"              : 32,
                   "channels"           : 3  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

    # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : True,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : False,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                            save_directory = save_directory,
                            preprocess_init_args = preprocess_params,
                            verbose = 3)
    return dataset

def cook_caltech101(verbose = 1, **kwargs):
    """
    Wrapper to cook cifar10 dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                    "source"             : 'skdata',
                    "name"               : 'caltech101',
                    "location"           : '',
                    "mini_batch_size"    : 72,
                    "mini_batches_per_batch" : (1, 1, 1),
                    "batches2train"      : 60,
                    "batches2test"       : 37,
                    "batches2validate"   : 30,
                    "height"             : 224,
                    "width"              : 224,
                    "channels"           : 3  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

        # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : False,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : False,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                        save_directory = save_directory,
                        preprocess_init_args = preprocess_params,
                        verbose = 3)
    return dataset

def cook_caltech256(verbose = 1, **kwargs):
    """
    Wrapper to cook cifar10 dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                    "source"             : 'skdata',
                    "name"               : 'caltech256',
                    "location"           : '',
                    "mini_batch_size"    : 36,
                    "mini_batches_per_batch" : (1, 1, 1),
                    "batches2train"      : 424,
                    "batches2test"       : 226,
                    "batches2validate"   : 200,
                    "height"             : 224,
                    "width"              : 224,
                    "channels"           : 3  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

        # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : False,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : False,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                        save_directory = save_directory,
                        preprocess_init_args = preprocess_params,
                        verbose = 3)
    return dataset

def cook_cifar10_normalized_zero_mean(verbose = 1, **kwargs):
    """
    Wrapper to cook cifar10 dataset. Will take as input,

    Args:

        save_directory: which directory to save the cooked dataset onto.
        dataset_parms: default is the dictionary. Refer to :mod:`setup_dataset`
        preprocess_params: default is the dictionary. Refer to :mod:`setup_dataset`
    """

    if not 'data_params' in kwargs.keys():

        data_params = {
                   "source"             : 'skdata',
                   "name"               : 'cifar10',
                   "location"			: '',
                   "mini_batch_size"    : 500,
                   "mini_batches_per_batch" : (80, 20, 20),
                   "batches2train"      : 1,
                   "batches2test"       : 1,
                   "batches2validate"   : 1,
                   "height"             : 32,
                   "width"              : 32,
                   "channels"           : 3  }

    else:
        data_params = kwargs['data_params']

    if not 'preprocess_params' in kwargs.keys():

    # parameters relating to preprocessing.
        preprocess_params = {
                            "normalize"     : True,
                            "ZCA"           : False,
                            "grayscale"     : False,
                            "zero_mean"     : True,
                        }
    else:
        preprocess_params = kwargs['preprocess_params']

    if not 'save_directory' in kwargs.keys():
        save_directory = '_datasets'
    else:
        save_directory = kwargs ['save_directory']

    dataset = setup_dataset(dataset_init_args = data_params,
                            save_directory = save_directory,
                            preprocess_init_args = preprocess_params,
                            verbose = 3)
    return dataset

cook_mnist = cook_mnist_normalized
cook_cifar10 = cook_cifar10_normalized

if __name__ == '__main__':
    pass
